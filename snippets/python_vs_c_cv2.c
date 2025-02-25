class MyObject {

public: // all that follows is public

MyObject( int arg ) {
    myprop = arg;
}

void printme() {
    cout << myprop;
}

private: // all that follows is private

int myprop;
}