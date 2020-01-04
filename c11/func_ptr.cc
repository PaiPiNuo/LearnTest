#include <iostream>

using namespace std;

int add(int a, int b) {
    return a+b;
}

class add_class {
	public:
		const int operator()(const int a, const int b) {
		    return a + b;
		}
};
int main() {
    int(*Addfunc1)(int a, int b);
    int(*Addfunc2)(int a, int b);

	Addfunc1 = add;
	Addfunc2 = &add;

	cout << Addfunc1(2, 3) << endl;
    cout << (*Addfunc2)(22, 33) << endl;
	
	cout << "-------function object------" << endl;
	add_class add_object;
	cout << add_object(11, 22) << endl;
	return 0;
}
