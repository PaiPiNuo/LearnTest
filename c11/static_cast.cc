#include <iostream>
using namespace std;

class A {
public:
	operator int() {return 1;}
	operator char*() {
		cout<<"A.operator char*()---"<<endl;
		return NULL;}

};

int main() {
    A a;
	int n;
	char* p = "Hello!";
	n = static_cast <int> (3.14);
	cout<<"static_cast <int> (3.14)---"<<n<<endl;;
	n = static_cast <int> (a);
	cout<<"static_cast <int> (a)---"<<n<<endl;
	p = static_cast <char*>(a);
	cout<<"static_cast <char*> (a)---"<<p<<endl;;
	return 0;
}
