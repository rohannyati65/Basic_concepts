
#include<iostream>
#include<algorithm>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while (t--)
    {
        int k,n;
        cin >> n;
        k = __gcd(n,100);
        cout << 100/k << endl;
    }
    
    return 0;
    
}