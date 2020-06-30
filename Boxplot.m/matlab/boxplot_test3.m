TreadmillData = randi([20,200],69,6);
Speeds = {'1.5mph' '2.5mph' '3.5mph' '4.5mph' '5.5mph' '6.5mph'};
DeviceColors = {'r' 'g' 'c' [0.5 0 0.5] 'b' [1 0.5 0]};
Pedometer1 = TreadmillData(1:7:end,:);
Pedometer2 = TreadmillData(2:7:end,:);
Pedometer3 = TreadmillData(3:7:end,:);
Pedometer4 = TreadmillData(4:7:end,:);
Pedometer5 = TreadmillData(5:7:end,:);
Pedometer6 = TreadmillData(6:7:end,:);

GroupedData = {Pedometer1 Pedometer2 Pedometer3 Pedometer4 Pedometer5 Pedometer6}; 

legendEntries = {'dev1' 'dev2' 'dev3' 'dev4' 'dev5' 'dev6'};

figure;
Xt = 20:20:120;
Xt_Offset = [-15,-10,-5,5,10,15];

for i=1:6 
    boxplot(GroupedData{i},'Color',DeviceColors{i});
    set(gca,'XTick',Xt+Xt_Offset(i));
    if i==3
        set(gca,'XTickLabel',Speeds);
    end
    hold on;
end
xlabel('Speed');ylabel('Step Count'); grid on;
legend(legendEntries);