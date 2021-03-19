#include<iostream>
#include<deque>


using namespace std;


class Stack
{
    private:
        deque<int> q1,q2;

    public:
        void push(const int& element);
        void pop();
        //int top();

};

void Stack::push(const int& element)
{
    this->q1.push_front(element);
}

void Stack::pop()
{
    if(this->q1.empty())
        if(this->q2.empty())
        {
            cout<<"Stack is empty\n";
        }
        else
        {
            for(int i = 1 ; i< this->q2.size(); i++)
                {
                    this->q1.push_front(this->q2.back());
                    this->q2.pop_back();
                }
            int x = this->q2.back();
            this->q2.pop_back();
            cout<<x<<" ";
        }
    else
    {
        for(int i = 1; i < this->q1.size(); i++)
            {
                this->q2.push_front(this->q1.back());
                this->q1.pop_back();
            }
        int x = this->q1.back();
        this->q1.pop_back();
        cout<<x<<" ";

    }
}


int main()
{
    Stack s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    s.push(6);
    s.pop();

    return 0;
}
