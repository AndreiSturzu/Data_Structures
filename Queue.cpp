#include<iostream>
#include<stack>
#include<deque>

using namespace std;

class Queue
{
    private:
        stack<int> stack1;
        stack<int> stack2;

    public:
        void push_back(const int& element);
        void pop_front();
        int get_front();
        void show();
};

// inserts element in Queue
void Queue::push_back(const int& element)
{
    this->stack1.push(element);
};

//removes element from Queue
void Queue::pop_front()
{
    if(this->stack1.empty())
        if(this->stack2.empty())
            cout<<"Queue is empty"<<endl;
        else
        {
            //cout<<this->stack2.top()<<" ";
            this->stack2.pop();
        }
    else
    {
        if(!this->stack2.empty())
        {
            this->stack2.pop();
        }
        else
        {
            while(!this->stack1.empty())
            {
                this->stack2.push(this->stack1.top());
                this->stack1.pop();
            }
            //cout<<this->stack2.top()<<" ";
            this->stack2.pop();
        }
    }
};

// returns element and removes element from Queue
int Queue::get_front()
{
    int first;
    if(this->stack1.empty())
        if(this->stack2.empty())
            cout<<"Queue is empty"<<endl;
        else
        {
            first = this->stack2.top();
            this->stack2.pop();
            return first;
        }
    else
    {
        while(!this->stack1.empty())
        {
            this->stack2.push(this->stack1.top());
            this->stack1.pop();
        }
        first = this->stack2.top();
        this->stack2.pop();
        return first;
    }
};

int main()
{
    Queue q;
    q.push_back(1);
    q.pop_front();
    q.push_back(2);
    q.pop_front();
    q.push_back(3);
    q.push_back(4);
    q.push_back(5);
    q.pop_front();
    q.pop_front();
    int a = q.get_front();
    cout<<"a = "<<a<<endl;
    q.pop_front();

    return 0;
}
