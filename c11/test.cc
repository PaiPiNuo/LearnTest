#include <iostream>
#include <typeinfo>

using namespace std;

class my_class {
public:
	operator int() { // function : convert int to class object
	    cout << "convert to int" << endl;
		return 1;
	}

    explicit operator double() {
	    cout <<"convert to double"<< endl;
		return 1.1;
	}
};

int main() {
    // cout<<"data type int a:"<<typeid(a).name()<<endl;
    my_class a;
	int i_a;
	cout << a << endl;
	i_a = (int)a;
	cout << "i_a value is : "<< i_a<<endl;
	cout<< "float i_a is : "<< (float)i_a<<endl;
	double double_a = (double)a;
	cout<<"double a is :"<<double_a<<endl;
    return 0;
}
