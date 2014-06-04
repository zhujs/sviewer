# -*- coding: utf-8 -*-

from gi.repository import Gtk, Gdk
from textFrame import textFrame

class PopupWin( Gtk.Window ):
	"""Implement the popup window shown in specific position"""
	def __init__(self, selectedText, windowType=Gtk.WindowType.TOPLEVEL,
			X=None, Y=None, **kwds):
		super( PopupWin, self).__init__(windowType, **kwds)
		self.selectedText = selectedText 

		self.connect( 'destroy', self._on_destroy, None )
		self.set_default_size( 300, 300 )
		self.set_title( selectedText )

		# create a scrolled window and pack it in the main window
		scrolledWin = Gtk.ScrolledWindow()
		scrolledWin.set_border_width(10)

		# always show the vertical scrollbar if necessary
		scrolledWin.set_policy( Gtk.PolicyType.NEVER,
				Gtk.PolicyType.AUTOMATIC )

		self.grid = Gtk.Grid()
		self.grid.set_orientation( Gtk.Orientation.VERTICAL )

		self._createMessageGrid( '百度百科','Test' )
		scrolledWin.add( self.grid )
		self.add( scrolledWin )
		self.show_all()
		# self.get_window().is_destroyed() 

		if X is not None and Y is not None:
			self.move( X + 10, Y + 10 )

	def _createMessageGrid( self, label, text ):
		"""function to create a textFrame which will be added into the grid
			label: Label shown in the frame header
			text: Message shown in the text View
		"""
		grid = Gtk.Grid()
		grid.set_orientation( Gtk.Orientation.VERTICAL )

		frame = textFrame( label ) 
		frame.addText( text )
		frame.set_hexpand( True )
		frame.set_halign( Gtk.Align.FILL )
		grid.add( frame  )

		
		# Show a link for the user to view the web page
		label=Gtk.Label()
		label.set_markup( '<a href="http://www.baidu.com">View More</a>')
		label.set_hexpand( True )
		label.set_halign( Gtk.Align.END )
		grid.add( label )
		
		self.grid.add( grid )

	def _on_destroy( self, widget, data ):
		widget.destroy()		

if __name__ == "__main__":
	win = PopupWin( 'power', X=200, Y=200)
	Gtk.main()

