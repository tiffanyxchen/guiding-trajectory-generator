
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

std::vector<std::vector<double>> simulate(
    const std::vector<double>& time,
    const std::vector<double>& x0,
    double g, double L, double m);

namespace py = pybind11;

PYBIND11_MODULE(cpp_bindings, m) {
    m.def("simulate", &simulate);
}
