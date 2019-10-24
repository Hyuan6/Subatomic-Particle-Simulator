#ifndef DATABASE
#define DATABASE

#include <string>
#include <unordered_map>

class Database{

public:
    Database(std::string);
    
    bool haskey(std::string);
    std::unordered_map<std::string, double> get(std::string);
    void write(std::string, std::unordered_map<std::string, double>);

private:
    std::unordered_map<std::string, std::unordered_map<std::string, double>> storage;
    std::string foldername = "db";

    bool checkFile(std::string);
	void readDb();
};

#endif