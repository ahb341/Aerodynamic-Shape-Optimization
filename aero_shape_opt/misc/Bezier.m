function Pts = Bezier(p, num_coords)
%Bezier returns the points of a Bezier curve
%   p = [x1 y1; x2 y2; xn yn]
%   num_coords = number of coordinates to be returned
clf;
n = length(p);
nm1 = n-1;
binom = zeros(1,n);
for i=0:1:nm1
    % binomial coeffs calculated using: (x!/(y!(x-y)!))
    binom(i+1)=factorial(nm1)/(factorial(i)*factorial(nm1-i));  
end
L = [];
UB = zeros(1,n);
for t=linspace(0,1,num_coords)
    for d=1:n
        UB(d)=binom(d)*((1-t)^(n-d))*(t^(d-1));
    end
    L=cat(1,L,UB);%catenation 
end
Pts=L*p;
line(Pts(:,1),Pts(:,2),'Color','red')
line(p(:,1),p(:,2))
end
