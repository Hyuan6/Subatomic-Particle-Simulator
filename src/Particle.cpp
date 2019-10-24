#include <Particle.hpp>
#include <unordered_map>

Particle::Particle(std::string type, Database* db){
    particleType = type;
    this->db = db;

    setData();
}

void Particle::setRadius(double r){
    radius = r;
}
double Particle::getRadius(){
    return radius;
}
void Particle::setMass(double m){
    mass = m;
}
double Particle::getMass(){
    return mass;
}
void Particle::setCharge(double c){
    charge = c;
}
double Particle::getCharge(){
    return charge;
}

void Particle::setPosition(double x, double y, double z){
   position = glm::vec4(x,y,z,1);
}
glm::vec4 Particle::getPosition(){
    return position;
}
void Particle::setVelocity(double x, double y, double z){
    velocity = glm::vec4(x, y, z, 0);
}
glm::vec4 Particle::getVelocity(){
    return velocity;
}
void Particle::setAcceleration(double x, double y, double z){
    acceleration = glm::vec4(x, y, z, 0);
}
glm::vec4 Particle::getAcceleration(){
    return acceleration;
}
void Particle::setData(){
    std::unordered_map<std::string, double> data = db->get(particleType);

    radius = data["radius"];
    radiusMagnitude = data["radiusMag"];
    mass = data["mass"];
    massMagnitude = data["massMag"];
    charge = data["charge"];
    chargeMagnitude = data["chargeMag"];
}