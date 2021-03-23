clear; clc; close all;

for i = 1:10000
    name = strcat('NN',num2str(i+10000));
    [cp,af] = genAirfoil();
    save_Airfoil(name,af,cp);
end