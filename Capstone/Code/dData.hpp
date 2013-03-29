#include <time.h>
#include <sstream>

template<class T>
class Data{

public:
	Data(value);
	~Data();

	bool InsertDB();

private:
	T Value;
	time_t TimeStamp;
	char* DBString;

}

Data::Data(value){

	Value = value;
	TimeStamp = TIMENOW;

	stringstream ss;

	ss << "INSERT INTO DB "

	}
