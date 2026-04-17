
#include <vector>
#include <cmath>

using Vec = std::vector<double>;
using Mat = std::vector<std::vector<double>>;

// dynamics function
Vec dx(const Vec& x, double g, double L, double m) {
    double t1=x[0], t2=x[1], t3=x[2];
    double p1=x[3], p2=x[4], p3=x[5];

    double c12 = cos(t1-t2);
    double c13 = cos(t1-t3);
    double c23 = cos(t2-t3);
    
    double s12 = sin(t1 - t2);
    double s13 = sin(t1 - t3);
    double s23 = sin(t2 - t3);

    double Delta = 112 - 81*c12*c12 + 81*c12*c13*c23 - 36*c13*c13 - 63*c23*c23;

    Vec A = {
        48 - 27*c23*c23, -54*c12 + 27*c13*c23, 81*c12*c23 - 72*c13,
        -54*c12 + 27*c13*c23, 84 - 27*c13*c13, 81*c12*c13 - 126*c23,
        81*c12*c23 - 72*c13, 81*c12*c13 - 126*c23, 336 - 243*c12*c12
    };

    Vec dtheta(3);
    dtheta[0] = (A[0]*p1 + A[1]*p2 + A[2]*p3)/(m*L*L*Delta);
    dtheta[1] = (A[3]*p1 + A[4]*p2 + A[5]*p3)/(m*L*L*Delta);
    dtheta[2] = (A[6]*p1 + A[7]*p2 + A[8]*p3)/(m*L*L*Delta);

    double dtheta1 = dtheta[0];
    double dtheta2 = dtheta[1];
    double dtheta3 = dtheta[2];
    
    double dp1 =
        -1.5*m*L*L*dtheta1*dtheta2*s12
        -0.5*m*L*L*dtheta1*dtheta3*s13
        -2.5*m*g*L*sin(t1);

    double dp2 =
        +1.5*m*L*L*dtheta1*dtheta2*s12
        -0.5*m*L*L*dtheta2*dtheta3*s23
        -1.5*m*g*L*sin(t2);

    double dp3 =
        +0.5*m*L*L*dtheta1*dtheta3*s13
        +0.5*m*L*L*dtheta2*dtheta3*s23
        -0.5*m*g*L*sin(t3);

    return {dtheta1, dtheta2, dtheta3, dp1, dp2, dp3};

}

// RK4 integrator
Mat simulate(const Vec& time, const Vec& x0, double g, double L, double m) {
    int n = time.size();
    Mat result(n, Vec(6));

    Vec x = x0;
    result[0] = x;

    for (int i=1; i<n; i++) {
        double dt = time[i] - time[i-1];

        Vec k1 = dx(x, g, L, m);

        Vec x2(6);
        for(int j=0;j<6;j++) x2[j]=x[j]+0.5*dt*k1[j];
        Vec k2 = dx(x2, g, L, m);

        Vec x3(6);
        for(int j=0;j<6;j++) x3[j]=x[j]+0.5*dt*k2[j];
        Vec k3 = dx(x3, g, L, m);

        Vec x4(6);
        for(int j=0;j<6;j++) x4[j]=x[j]+dt*k3[j];
        Vec k4 = dx(x4, g, L, m);

        for(int j=0;j<6;j++){
            x[j] += dt/6.0*(k1[j]+2*k2[j]+2*k3[j]+k4[j]);
        }

        result[i]=x;
    }

    return result;
}
