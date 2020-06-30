#include "Yamahack.h"
#include <iostream>
using namespace std;

YamaHack::YamaHack(QString ip)
{
    buff = new char(10);
   // tcpsock = new QTcpSocket();
    this->ip = ip;
    sync=1;
    speedLeft = 0;
    speedRight = 0;
    setLeft = 0;
    setRight = 0;
    setAcl = 0;
    for (int i=0;i<10;i++){
        buff[i]=0;
    }
    connected=0;
}


bool YamaHack::connectS(){
    if (!connected){
        tcpsock = new QTcpSocket();
        tcpsock->connectToHost(ip, 12345);
        connect(tcpsock,SIGNAL(readyRead()),this,SLOT(slotReadyRead()));
        connected=1;
        qDebug() << "Connected";
        setspark();

    }
}

bool YamaHack::dis_connect(){
    if (connected){
        tcpsock->disconnectFromHost();
        disconnect(tcpsock,SIGNAL(readyRead()),this,SLOT(slotReadyRead()));
        delete tcpsock;
        connected=0;
        qDebug() << "Disconnected";

    }
}

void YamaHack::slotDisconnected(){

}
void YamaHack::slotConnected(){
}


void YamaHack::slotReadyRead(){
    tcpsock->read(buff,10);
    char transmission[10];
    sync = buff[0]+1;
    cout << QString::number(sync).toStdString() <<endl;
    transmission[0] = sync;
    transmission[1] = *((char*)(&setLeft)+0);
    transmission[2] = *((char*)(&setLeft)+1);
    transmission[3] = *((char*)(&setRight)+0);
    transmission[4] = *((char*)(&setRight)+1);
    transmission[5] = setAcl;
    transmission[6] = 111;
    transmission[7] = 222;
    transmission[8] = 333;
    transmission[9] = 444;
    tcpsock->write(transmission,10);
    speedLeft = *((int16_t*)(buff+1));
    speedRight  = *((int16_t*)(buff+3));
    SBar1 = buff[5];
    SBar2 = buff[6];
}
float YamaHack::getSpeedLeft(){
    return (float)speedLeft/152.4;
}
float YamaHack::getSpeedRight(){
    return (float)speedRight/152.4;
}
uint8_t YamaHack::getSensorBar1(){
    return SBar1;
}
uint8_t YamaHack::getSensorBar2(){
    return SBar2;
}


void YamaHack::setspark(){
    char transmission[]={0x01,0,0,0,0,0,0,0,0,0};
    tcpsock->write(transmission,10);
}


void YamaHack::setControl(int16_t left, int16_t right, uint8_t acl){
    this->setLeft = left;
    this->setRight = right;
    this->setAcl = acl;
}
