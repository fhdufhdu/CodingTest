#include <iostream>
using namespace std;
//https://www.acmicpc.net/problem/1011
//재귀함수 - 메모리 초과
//공식 : a[0] = 1, a[1] = a[0] + 1, a[2] = a[1] + 1, a[3] = a[2] + 2, a[4] = a[3] + 2, ... 의 규칙대로 움직임

long getCount(long a)
{
    long s = 1;
    long pre_sum = 0;
    long sum = 0;
    for (long i = 0; i < a; i++)
    {
        sum += s;
        if (i % 2 == 0 && i != 0)
        {
            s += 1;
        }

        if (pre_sum <= a && a < sum)
            return i;

        pre_sum = sum;
    }
}

int main()
{
    int n = 0;
    cin >> n;
    long *t = new long[n];

    for (int i = 0; i < n; i++)
    {
        long x, y;
        cin >> x >> y;
        t[i] = y - x;
    }

    for (int i = 0; i < n; i++)
    {
        cout << getCount(t[i]) << endl;
    }
}