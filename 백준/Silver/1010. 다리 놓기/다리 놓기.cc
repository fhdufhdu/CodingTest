#include <iostream>
using namespace std;
//https://www.acmicpc.net/problem/1010

long long getFactorial(int a, int b)
{
    long long r = 1;
    for (int i = a; i > b; i--)
    {
        r *= i;
    }

    return r;
}

int main()
{
    int cnt;
    int c[100000];
    cin >> cnt;

    for (int i = 0; i < cnt * 2; i++)
    {
        cin >> c[i];
    }

    for (int i = 0; i < cnt; i++)
    {
        int a = c[i * 2];
        int b = c[i * 2 + 1];
        long long r;
        if (a < b)
        {
            if (a >= b - a)
            {
                r = getFactorial(b, a) / getFactorial(b - a, 0);
            }
            else
            {
                r = getFactorial(b, b - a) / getFactorial(a, 0);
            }
        }
        else if (a = b)
        {
            r = 1;
        }
        else
        {
            if (b >= a - b)
            {
                r = getFactorial(a, b) / getFactorial(a - b, 0);
            }
            else
            {
                r = getFactorial(a, a - b) / getFactorial(b, 0);
            }
        }
        cout << r << endl;
    }
}