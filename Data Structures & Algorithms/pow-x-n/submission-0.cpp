class Solution {
public:
    double myPow(double x, int n) {
        long binary = n;
        double pow = 1;

        if (binary < 0) {
            binary = -n;
            x = 1/x;
        }

        while (binary > 0) {
            if (binary % 2 == 1) {
                pow *= x;
            }

            x *= x;
            binary /= 2;
        }

        return pow;
    }
};
