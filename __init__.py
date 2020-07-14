# Hides the Stats button and disables the shortcut

#Autor: Hector Diaz https://github.com/raro28/anki-hide-stats

from aqt import gui_hooks
from aqt.toolbar import Toolbar
from aqt import mw
from anki.lang import _
from aqt.qt import QShortcut

def _centerLinks(self) -> str:
        links = [
                self.create_link(
                "decks",
                _("Decks"),
                self._deckLinkHandler,
                tip=_("Shortcut key: %s") % "D",
                id="decks",
                ),
                self.create_link(
                "add",
                _("Add"),
                self._addLinkHandler,
                tip=_("Shortcut key: %s") % "A",
                id="add",
                ),
                self.create_link(
                "browse",
                _("Browse"),
                self._browseLinkHandler,
                tip=_("Shortcut key: %s") % "B",
                id="browse",
                ),
        ]

        links.append(self._create_sync_link())

        gui_hooks.top_toolbar_did_init_links(links, self)

        return "\n".join(links)

Toolbar._centerLinks = _centerLinks
#https://github.com/Liresol/anki-custom-shortcuts/blob/663d692410e7601e75d8ff6497478460e005abcc/custom_shortcuts/custom_shortcuts.py
qshortcuts = mw.findChildren(QShortcut)
for scut in qshortcuts:
        if scut.key().toString() == "T":
                scut.setEnabled(False)