#include <iostream>
#include <time.h>
using namespace std;
//https://www.acmicpc.net/problem/1010

int fibonacci(int n, int a[][3])
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        if (a[n - 1][0] != -1 && a[n - 2][0] != -1)
        {
            a[n][0] = a[n - 1][0] + a[n - 2][0];
        }
        else if (a[n - 1][0] != -1)
        {
            a[n][0] = a[n - 1][0] + fibonacci(n - 2, a);
        }
        else if (a[n - 2][0] != -1)
        {
            a[n][0] = fibonacci(n - 1, a) + a[n - 2][0];
        }
        else
        {
            a[n][0] = fibonacci(n - 1, a) + fibonacci(n - 2, a);
        }
        a[n][1] = a[n - 1][1] + a[n - 2][1];
        a[n][2] = a[n - 1][2] + a[n - 2][2];
        return a[n][0];
    }
}

int main()
{
    int fibo[41][3];
    for (int i = 0; i < 41; i++)
    {
        fibo[i][0] = -1;
        fibo[i][1] = 0;
        fibo[i][2] = 0;
    }

    fibo[0][0] = 0;
    fibo[0][1] = 1;
    fibo[0][2] = 0;
    fibo[1][0] = 1;
    fibo[1][1] = 0;
    fibo[1][2] = 1;

    int n;
    cin >> n;
    int *arr = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++)
    {
        fibonacci(arr[i], fibo);
        cout << fibo[arr[i]][1] << " " << fibo[arr[i]][2] << endl;
    }

    return 0;
}