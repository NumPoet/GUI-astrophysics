#ifndef COLHYPOD_H
#define COLHYPOD_H

#include <QMainWindow>

namespace Ui {
class colhypod;
}

class colhypod : public QMainWindow
{
    Q_OBJECT

public:
    explicit colhypod(QWidget *parent = 0);
    ~colhypod();

private:
    Ui::colhypod *ui;
};

#endif // COLHYPOD_H
