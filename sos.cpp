#include <iostream>
using namespace std;

int *x, *w, n, m;

void display(int k) {
	for(int i=0; i<=k ;i++) {
		cout<<x[i]<<" ";
	}
	for(int i=k+1; i<n; i++) {
		cout<<"0 ";
	}
	cout<<endl;
}

void SumofSubsets(int s, int k, int r) {
	x[k] = 1;
	
	if(s+w[k]==m)
		display(k);
	else if(s+w[k]+w[k+1]<=m)
		SumofSubsets(s+w[k], k+1, r-w[k]);
	
	if(s+r-w[k]>=m && s+w[k+1]<=m) {
		x[k] = 0;
		SumofSubsets(s, k+1, r-w[k]);
	}
}

int main() {
	int r = 0;
	cin>>n>>m;
	w = new int[n];
	x = new int[n];
	for(int i=0; i<n; i++) {
		cin>>w[i];
		r += w[i];
	}
	SumofSubsets(0, 0, r);
	delete[] x;
	delete[] w;
	return 0;
}