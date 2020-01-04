#include <iostream>
#include <memory>

using namespace std;

class A {
public:
	int i;
	A(int n):i(n) {};
	~A() {cout<<i<<" "<<" destructed"<<endl;}
};

int main() {
    shared_ptr<A> sp1(new A(2)); // A(2) is managed by sp1
	shared_ptr<A> sp2(sp1);
	shared_ptr<A> sp3;
	sp3 = sp2;
	cout << sp1->i<< "," << sp2->i << ","<< sp3->i << endl;
	cout << "-------------------------" << endl;
	A* p = sp3.get();
	cout << p->i << endl;
	sp1.reset(new A(3));
	sp2.reset(new A(4));
	cout << sp1->i << endl;
	sp3.reset(new A(5));
	cout << "end" << endl;
	return 0;
}
