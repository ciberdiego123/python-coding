#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    int worms[n];
    int s[n];
    for (int i = 0; i < n; i++) {
        cin>>worms[i];
        if(i == 0)
            s[i] = worms[i];
        else
            s[i] = s[i-1] + worms[i];
    }
    int k;
    cin>>k;
    for (int l = 0; l < k; l++) {
        int c;
        cin >> c;
        int i = 0;
        int j = n-1;
        while(j-i>0){
            int bm = i + (j-i+1) / 2;
            int m;
            if(bm==j)
                m=j-1;
            else if(bm==i)
                m=i+1;
            else
                m=bm;
            if(s[m]>c)
                j = m;
            else
                i = m;
            if(j - i == 1){
                if(s[i] < c && c <= s[j]){
                    i = j;
                }else{
                    j = i;
                }
            }
        }
        cout<<i+1<<endl;
    }
}
