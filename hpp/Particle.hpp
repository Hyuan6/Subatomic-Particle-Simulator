#ifndef PARTICLE
#define PARTICLE

#include <string>
#include <Database.hpp>
#include <glm/glm.hpp>

class Particle{

public:
    Particle(std::string, Database*);

    void setRadius(double);
    double getRadius();
    void setMass(double);
    double getMass();
    void setCharge(double);
    double getCharge();

    glm::vec4 getPosition();
    glm::vec4 getVelocity();
    glm::vec4 getAcceleration();

private:
    double radius;
    double radiusMagnitude;
    double mass;
    double massMagnitude;
    double charge;
    double chargeMagnitude;

    Database* db;
    std::string particleType;

    glm::vec4 position;
    glm::vec4 velocity;
    glm::vec4 acceleration;

    void setPosition(double, double, double);
    void setVelocity(double, double, double);
    void setAcceleration(double, double, double);

    void setData();
};

#endif