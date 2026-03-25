class MyQueue {
    Stack<Integer> st1;
    Stack<Integer> st2;
    public MyQueue() {
        this.st1 = new Stack<>();
        this.st2 = new Stack<>();
    }
    
    public void push(int x) {
        this.st1.push(x);
    }
    
    public int pop() {
        shift();
        return this.st2.pop();
    }
    
    public int peek() {
        shift();
        return this.st2.peek();
    }
    
    public boolean empty() {
        return this.st1.isEmpty() && this.st2.isEmpty();
    }
    private void shift(){
        if(this.st2.isEmpty()){
            while(!this.st1.isEmpty()){
                this.st2.push(st1.pop());
            }
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */