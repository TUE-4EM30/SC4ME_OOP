class MyObject {
    void MyObject( int arg ) {
        myprop = arg;
    }
    // equals (a == b) as method
    MyObject operator==(const MyObject& other) {
        return myprop == other.myprop;
    }
    
    int myprop;
    }
    
    // addition (a + b) as external function
    MyObject operator+( const MyObject& a, const
        MyObject& b ) {
        return MyObject( a.myprop + b.myprop );
    }
