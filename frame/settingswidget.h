#ifndef SETTINGSWIDGET_H
#define SETTINGSWIDGET_H

#include "contentwidget.h"
#include "moduleinterface.h"

#include <QMap>
#include <QVBoxLayout>

class Frame;
class SettingsWidget : public ContentWidget, public FrameProxyInterface
{
    Q_OBJECT

public:
    explicit SettingsWidget(Frame *frame);

public slots:
    void contentPopuped(ContentWidget * const w);
    void pushWidget(ModuleInterface * const inter, ContentWidget * const w);

private slots:
    void loadModule(ModuleInterface * const module);

private:
    Frame *m_frame;

    QVBoxLayout *m_settingsLayout;
    QWidget *m_settingsWidget;

    QList<ModuleInterface *> m_moduleInterfaces;
    QMap<ModuleInterface *, QList<ContentWidget *>> m_moduleWidgets;
};

#endif // SETTINGSWIDGET_H