#include <iostream>
using namespace std;

long long fib(int n) {
    long long ffirst = 0;
	long long fsecond = 1;
	int i;
	if (n > 0) {
	    for (i = 1; i < n; i++) {
    		ffirst += fsecond;
    		fsecond = ffirst - fsecond;
    		ffirst -= fsecond;
    		fsecond = ffirst + fsecond;
	    }
	    return fsecond;
    }
	else if (n < 0) {
	    for (i = 0; i > n; i--) {
	        ffirst += fsecond;
		    fsecond = ffirst - fsecond;
		    ffirst -= 2 * fsecond;
	    }
	    return ffirst;
	}
	return 0;
}

int main() {
	int i;
	int j;
	long long mul = 0;
	for (i = 2; i <= 100; i++) {
		long long fi = fib(i);
		for (j = 2; j <= i; j++) {
			long long fj = fib(j);
			long long quot = div(j - 2, 2).quot;
			int rest = (j - 2) % 2;
			mul = fib(2 + 4 * quot + 2 * rest + i - j) + fib(2 + i - j - rest) * rest;
			long long count = 0;
			for (count = 0; count < quot; count++) {
				mul += fib(2 + 4 * count + 2 * rest + i - j);
			}
			if (mul == fi * fj) {
				cout << "correct for: " << fi << ", " << fj << endl;
			}
			else {
			    cout << quot << " wrong for " << fi << ", " << fj << " ans = " << mul << " correct = " << fi * fj << endl;
			}
		}
	}
	return 0;
}