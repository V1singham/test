#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
       long long int x1,y1,z1,r1,c1,sum=0;
        cin>>x1>>y1>>z1;
        int arr1[x1+2][y1+2];
      for(int j1=0;j1<=(x1+1);j1++)
        {
            for(int k1=0;k1<=(y1+1);k1++)
            {
             arr1[j1][k1]=0;
           }
        }
        for(int i1=0;i1<z1;i1++){
            cin>>r1>>c1;
            arr1[r1][c1]=1;
        }

        for(int e1=0;e1<=(x1+1);e1++)
        {
            for(int f1=0;f1<=(y1+1);f1++)
            {
              if(arr1[e1][f1]==1)
              {
                  if(arr1[e1+1][f1]==0){
                   sum++;

                  }
                  if(arr1[e1][f1+1]==0){
                  sum++;

                  }
                  if(arr1[e1-1][f1]==0){
                  sum++;

                  }
                  if(arr1[e1][f1-1]==0){
                  sum++;

                  }
              }
            }

        }
       cout<<sum<<endl;
    }
}
