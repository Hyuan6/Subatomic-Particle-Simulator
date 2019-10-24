#include <Database.hpp>
#include <fstream>
#include <boost/filesystem.hpp>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <string>

void tokenize(std::string const &str, const char delim, std::vector<std::string> &out){
	size_t start;
	size_t end = 0;

	while ((start = str.find_first_not_of(delim, end)) != std::string::npos)
	{
		end = str.find(delim, start);
		out.push_back(str.substr(start, end - start));
	}
}

Database::Database(std::string filename){

}

bool Database::haskey(std::string s){
    return storage.find(s) != storage.end();
}
std::unordered_map<std::string, double> Database::get(std::string s){
    auto pos = storage.find(s);
    if(pos != storage.end()){
        return storage[s];
    }else{
        return NULL;
    }
}
void Database::write(std::string s, std::unordered_map<std::string, double> data){

}
bool Database::checkFile(std::string s){
    namespace fs = boost::filesystem;
	
	fs::path full_path( fs::initial_path<fs::path>() );
    full_path = fs::system_complete( fs::path( foldername ) );
	return fs::is_regular_file(full_path);
}
void Database::readDb(){
    namespace bs = boost::filesystem;
    
    if(!bs::exists(foldername)){
        std::cout << "Error: Database folder does not exists." << std::endl;
        
        //TODO:: Implement better throw message.
        throw 0;
    }

    bs::directory_iterator end_itr;

    std::ifstream inFile(foldername);

	std::string line;

	while (inFile >> line){
		std::vector<std::string> items;
        std::unordered_map<std::string, double> data;

		tokenize(line, ' ', items);

        std::string particleType = items[0];
        double radius = atof(items[1].c_str());
        double mass = atof(items[2].c_str());
        double charge = atof(items[3].c_str());

        data["radius"] = radius;
        data["mass"] = mass;
        data["charge"] = charge;

		storage.insert({particleType, data});
	}
}