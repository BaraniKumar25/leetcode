// Last updated: 7/14/2026, 10:11:25 AM
class MinStack {
    Stack<Integer> a = new Stack<>();
    Stack<Integer> b=new Stack<>();
    public void push(int val) {
        a.push(val);
        if(b.isEmpty())
        {
            b.push(val);
        }
        else if(val<=b.peek())
        {
            b.push(val);
        }
    }
    public void pop() {
       int num=a.pop();
       if(!b.isEmpty())
       {
        if(num==b.peek())
        {
            b.pop();
        }
       }
    }
    public int top() {
        return a.peek();
    }
    public int getMin() {
        if(!b.isEmpty())
        return b.peek();
        else
        return 0;
        
    }
}
