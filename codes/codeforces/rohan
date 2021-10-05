#include<iostream>
#include<bits/stdc++.h>
#include<math.h>
using namespace std;


int highestPowerof2(int n) {
    int p = (int)log2(n);
    return (int)pow(2,p);
}
int main(){
    int n,t;
    cin >>t;
    while(t--){
        cin >> n;
        n=highestPowerof2(n);
        cout << n-1 << endl;
        /*
        if(n==1){
            cout << "0"<< endl;
        }
        else{
            if(highestPowerof2(n)){
                cout << n-1;
                break;
            }
            else{
                for(int i=n-1;i>=2;i--){
                    if(highestPowerof2(i)){
                        cout << i-1<< endl;
                        break;
                    }
                }
            }
        }*/
    }
    return 0;
}