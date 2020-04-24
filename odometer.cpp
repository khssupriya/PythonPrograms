#include<bits/stdc++.h>
#include<string>
using namespace std;

class odometer{
private:
	string DIGITS="123456789";
	int MinReading,MaxReading,CurrReading;
public:
	int size;
	odometer(int size){
		this->size=size;
		MinReading=stoi(DIGITS.substr(0,size));
		MaxReading=stoi(DIGITS.substr(9-size));
		CurrReading=MinReading;
	}	
	bool isAscending(int n){
	    int prev = 10; 
	    while (n){ 
	        int rem = n % 10; 
	        n /= 10; 
	        if (rem >=prev) 
	           return false; 
	        prev = rem; 
	    }
	    return true; 
	} 
	int GetNextReading(){
	    if (CurrReading==MaxReading)
            return MinReading;
        int AssumedReading=CurrReading+1;
        while(!isAscending(AssumedReading))
            AssumedReading+=1;
        CurrReading=AssumedReading;
        return CurrReading;
	}
	int GetPrevReading(){
		if (CurrReading==MinReading)
            return MaxReading;
        int AssumedReading=CurrReading-1;
        while(!isAscending(AssumedReading))
            AssumedReading-=1;
        CurrReading=AssumedReading;
        return CurrReading;
	}
	int GetNextNthReading(int n){
		for(int i=0;i<n;i++)
			CurrReading=GetNextReading();
		return CurrReading;
	} 
	int GetPrevNthReading(int n){
		for(int i=0;i<n;i++)
			CurrReading=GetPrevReading();
		return CurrReading;
	} 
	int DiffernceInReadings(int readingA, int readingB){
		CurrReading=readingA;
		int diff=0;
		while(GetNextReading()<readingB)
			diff++;
		return diff;
	}
};

int main()
{
 	odometer o(3);
 	cout<<o.GetNextReading()<<" "<<o.GetNextNthReading(3)<<" "<<o.GetPrevReading()<<endl;
 	cout<<o.GetPrevNthReading(2)<<" "<<o.DiffernceInReadings(347,359)<<endl;
    return 0;
}
