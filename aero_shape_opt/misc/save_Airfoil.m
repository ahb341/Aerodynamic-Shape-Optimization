function save_Airfoil(name,af,cp)
% af: coordinates

filename = strcat('.\airfoil_gen\', name);

% Remove files of the same name from the directory
[status,result] =dos(strcat('del ',filename,'.dat'));

% Write airfoil name and coords to dat file
fid = fopen(strcat(filename,'.dat'), 'w');
fprintf(fid, strcat(name,'\n'));
for i=1:length(af)
    fprintf(fid, '%2.8f  %2.8f\n',...
        af(i,1), af(i,2));
end
fclose(fid);

filename = strcat(filename,'_CP');
fid = fopen(strcat(filename,'.dat'),'w');
fprintf(fid, strcat(name,'\n'));
for i = 1:length(cp)
    fprintf(fid, '%2.8f  %2.8f\n',...
        cp(i,1), cp(i,2));
end
fclose(fid);

end