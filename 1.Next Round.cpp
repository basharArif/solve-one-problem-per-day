#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,k,a,b=0,arr[100];
    cin >> n >> k;
    for(int i=1; i<=n; i++)
    {
        cin >> a;
        arr[i] = a;
    }
    for(int j=1; j<=n; j++)
    {
        if(arr[j] >= arr[k] && arr[j] > 0)
        {
            b++;
        }
    }
    cout << b;

    return 0;
}
