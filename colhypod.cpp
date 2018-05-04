#include "colhypod.h"
#include "ui_colhypod.h"

colhypod::colhypod(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::colhypod)
{
    ui->setupUi(this);
}

colhypod::~colhypod()
{
    delete ui;
}
