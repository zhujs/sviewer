
from gi.repository import Gtk, Gdk

class PopupWin( Gtk.Window ):
	"""Implement the popup window shown in specific position"""
	def __init__(self, text, windowType=Gtk.WindowType.TOPLEVEL,
			X=None, Y=None, **kwds):
		super( PopupWin, self).__init__(windowType, **kwds)
		self.text = text 

#		self.connect("delete-event", self.hide_on_delete )
		self.set_default_size( 300, 300 )
		self.set_title(text)

		# create a scrolled window and pack it in the main window
		scrolledWin = Gtk.ScrolledWindow()
		scrolledWin.set_border_width(10)

		# always show the vertical scrollbar if necessary
		scrolledWin.set_policy( Gtk.PolicyType.NEVER,
				Gtk.PolicyType.ALWAYS )

		
		self.show_all()

		if X is not None and Y is not None:
			self.move( X + 10, Y + 10 )


if __name__ == "__main__":
	win = PopupWin( X=200, Y=200)
	Gtk.main()

	


