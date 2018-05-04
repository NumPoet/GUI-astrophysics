#include "colhypod.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    colhypod w;
    w.show();

    return a.exec();
}
