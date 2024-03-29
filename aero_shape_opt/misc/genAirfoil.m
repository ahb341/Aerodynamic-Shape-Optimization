function [cp,af] = genAirfoil()
%order = 6; % order of Bezier curve
num_coords = 70;

% Airfoil is defined by
%  LEU = Leading edge up            LED = Leading edge down
%  C25 = Camber at 25%              T25 = Thickness at 25%
%  C50 = Camber at 50%              T50 = Thickness at 50%
%  C75 = Camber at 75%              T75 = Thickness at 75%

% CONSTRAINTS
%          LEU   LED     C25   C50    C75      T25   T50   T75
genmaxs = [0.2,  0.2,    0.15,  0.15,   0.15,  0.25,  0.25,  0.2];
genmins = [0.0,  0.0,    0.0,  0.0,   0.0,     0.0,  0.0,  0.0];
% Generate Airfoil
% Generate random values within constraints
gen = zeros(1,length(genmaxs));

for i=1:length(genmaxs)
    gen(i) = rand*(genmaxs(i)-genmins(i))-genmins(i);
end
[cp,af] = genControlPoints(gen,num_coords);

end

