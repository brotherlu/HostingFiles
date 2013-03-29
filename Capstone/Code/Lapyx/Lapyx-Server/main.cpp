#include <iostream>
#include <socket.h>
#include <un.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof((a)[0]))

int main (void){

if(connect()==-1)
	std::cout<<"Could not create"<<std::endl;


return 0;

}
