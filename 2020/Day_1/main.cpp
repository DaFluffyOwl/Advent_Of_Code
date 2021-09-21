#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int Part_One(std::vector<int> num){
	for(int i = 0; i < num.size(); i++){
		for(int j = 0; j < num.size(); j++){
			if(num[i] + num[j] == 2020){
				int Answer = num[i] * num[j];
				cout << "Answer is: " << Answer << endl;
				return 0;
			}
		}
	}
	return -1;

}

int Part_Two(std::vector<int> num){
	for(int i = 0; i < num.size(); i++){
		for(int j = 0; j < num.size(); j++){
			for(int k = 0; k < num.size(); k++){
				if(num[i] + num[j] + num[k] == 2020){
					int Answer = num[i] * num[j] * num[k];
					cout << "Answer 2 is: " << Answer << endl;
					return 0;
				}
			}
		}
	}
	return -1;
}

int main(){
	int line;
	std::vector<int> arr = { };
	ifstream input;
	input.open("input.txt");
	cout << "File Opened\n";
	while(input >> line){
		arr.push_back(line);
	}

	Part_One(arr);
	Part_Two(arr);

	input.close();
	cout << "File Closed\n";
	return 0;
}