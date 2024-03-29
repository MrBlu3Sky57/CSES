#include <iostream>
#include <set>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    int x;
    set<pair<int, int>> s;

    for (int i = 0; i < n; i++)
    {
        cin >> x;
        s.insert({x, i});
    }

    for (int i = 0; i < m; i++)
    {
        cin >> x;
        auto it = s.lower_bound({x+1, 0});
        if (it != s.begin())
        {
            it--;
            cout << it->first << "\n";
            s.erase(it);
        }
        else
        {
            cout << "-1" << "\n";
        }
    }
}