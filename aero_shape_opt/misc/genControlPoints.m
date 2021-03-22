function [cp,af] = genControlPoints(gen,num_coords)
    % Define x and y control points for upper and lower curves
    upx = [0 0 0.25 0.5 0.75 1];
    downx = upx;

    upy = zeros(1,6);
    downy = zeros(1,6);
    
    % Leading edge
    upy(2) = gen(1);
    downy(2) = -gen(2);

    %Camber + thickness
    upy(3) = gen(3) + gen(6);
    upy(4) = gen(4) + gen(7);
    upy(5) = gen(5) + gen(8);

    downy(3) = gen(3) - gen(6);
    downy(4) = gen(4) - gen(7);
    downy(5) = gen(5) - gen(8);
    
    upper = []; lower = [];
    n = length(upx);
    for i = 1:n
        upper(i,:) = [upx(n-i+1) upy(n-i+1)];
        lower(i,:) = [downx(i) downy(i)];
    end
    cp = [upper; lower];
    af = [Bezier(upper, num_coords); Bezier(lower, num_coords)];
end
