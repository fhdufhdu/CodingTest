#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    bool prime[1001];
    for (int i = 0; i < 1001; i++)
        prime[i] = 1;

    prime[0] = false;
    prime[1] = false;

    for (int i = 2; i < (int)sqrt(1001); i++)
    {
        if (prime[i])
        {
            int cnt = i * i;
            while (cnt < 1001)
            {
                prime[cnt] = false;
                cnt += i;
            }
        }
    }

    int n;
    cin >> n;

    int result = 0;
    for (int i = 0; i < n; i++)
    {
        int input;
        cin >> input;

        if (prime[input])
            result++;
    }
    cout << result;
}