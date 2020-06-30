TreadmillData = randi([20,200],69,8);
Speeds = {'1.5mph' '2.5mph' '3.5mph' '4.5mph' '5.5mph' '6.5mph' '7.5mph' '8.5mph'};
DeviceColors = {'r' 'g' 'c' [0.5 0 0.5] 'b' [1 0.5 0]};
Pedometer1 = TreadmillData(1:7:end,:);
Pedometer2 = TreadmillData(2:7:end,:);
Pedometer3 = TreadmillData(3:7:end,:);
Pedometer4 = TreadmillData(4:7:end,:);
Pedometer5 = TreadmillData(5:7:end,:);
Pedometer6 = TreadmillData(6:7:end,:);
Pedometer7 = TreadmillData(7:7:end,:);
Pedometer8 = TreadmillData(8:7:end,:);

disp('TreadmillData is:')
disp(TreadmillData)
size(TreadmillData)

disp('Pedometer1 is:')
disp(Pedometer1)
size(Pedometer1)

GroupedData = {Pedometer1 Pedometer2 Pedometer3 Pedometer4 Pedometer5 Pedometer6 Pedometer7 Pedometer8}; 
disp('size of GroupedData')
disp(size(GroupedData))

legendEntries = {'dev1' 'dev2' 'dev3' 'dev4' 'dev5' 'dev6'};

N = numel(GroupedData);
delta = linspace(-.3,.3,N); %// define offsets to distinguish plots
width = .2; %// small width to avoid overlap
cmap = hsv(N); %// colormap
legWidth = 1.8; %// make room for legend

disp('N')
disp(N)

disp('delta is:')
disp(delta)

figure;
hold on;

for ii=1:8
    labels = Speeds; %// center plot: use real labels
    disp(labels)
    disp('position')
    disp((1:numel(labels))+delta(ii))
    disp('GroupedData{ii}')
    disp(GroupedData{ii})
    boxplot(GroupedData{ii},'Color', DeviceColors{ii}, 'boxstyle','filled', ...
        'position',(1:numel(labels))+delta(ii), 'widths',width, 'labels',labels)
        %// plot filled boxes with specified positions, widths, labels
    plot(NaN,1,'color',DeviceColors{ii}); %// dummy plot for legend
end
xlabel('Speed'); ylabel('Step Count'); grid on;
xlim([1+2*delta(1) numel(labels)+legWidth+2*delta(N)]) %// adjust x limits, with room for legend

legend(legendEntries);
