% Function that saves a .png file of a filled airfoil give a coordinate
% file
%

function save_Airfoil(airfoil)
    
    data = importdata([airfoil,'.dat']).data;
    fig = figure('visible','off');
    fill(data(:,1),data(:,2),'r');
    axis equal;
    set(gca,'XColor', 'none','YColor','none');
    exportgraphics(fig,[airfoil,'.png'],'Resolution',400); % save image as 400 dpi

end