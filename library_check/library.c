#include <string.h>

double convert_SI(double val, char *unit_in, char *unit_out) {
    double SI[8] = {0.001, 0.01, 1.0, 1000.0, 1609.34, 0.9144, 0.3048, 0.0254};
    char *units[8] = {"mm", "cm", "m", "km", "mile", "yard", "foot", "inch"};
    int i;
    double in_val = 0.0;
    double out_val = 0.0;
    for (i = 0; i < 8; i++) {
        if (strcmp(units[i], unit_in) == 0) {
            in_val = SI[i];
        }
        if (strcmp(units[i], unit_out) == 0) {
            out_val = SI[i];
        }
    }
    return val * in_val / out_val;
}
