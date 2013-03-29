class NavPath {

public:

private:

	int order;
	int *knotV;

	NavPoint *cPoint;


};

typedef struct {

	double latitude;	//x
	double longitude;	//y
	double altitude;	//z

} NavPoint;
