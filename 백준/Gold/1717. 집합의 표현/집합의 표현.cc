#include <bits/stdc++.h>

using namespace std;

vector<int> find_parent(int *data, int a)
{
    int cnt = 0;
    while (data[a] != a)
    {
        a = data[a];
        cnt++;
    }
    vector<int> result;
    result.push_back(a);
    result.push_back(cnt);

    return result;
}

void union_set(int *data, int a, int b)
{
    vector<int> ap = find_parent(data, a);
    vector<int> bp = find_parent(data, b);

    if (ap[1] < bp[1])
    {
        data[ap[0]] = bp[0];
    }
    else
    {
        data[bp[0]] = ap[0];
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m;
    cin >> n >> m;

    int data[1000001];
    for (int i = 0; i < 1000001; i++)
    {
        data[i] = i;
    }

    for (int i = 0; i < m; i++)
    {
        int o, a, b;
        cin >> o >> a >> b;

        if (o == 0)
        {
            union_set(data, a, b);
        }
        else if (find_parent(data, a)[0] == find_parent(data, b)[0])
        {
            cout << "YES\n";
        }
        else
        {
            cout << "NO\n";
        }
    }
}