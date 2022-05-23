/**
 * Moves Atomic Blocks Post Grid dates inside featured images.
 *
 * @package StudioPress\JS
 * @author StudioPress
 * @license GPL-2.0-or-later
 */

( function() {
	'use strict';

	/**
	 * Moves the Atomic Blocks Post Grid date element into the featured image.
	 *
	 * The desired styling can not be achieved without moving the element.
	 *
	 * @since 3.4.0
	 */
	function moveDates() {
		var i, $date, $imageLink;
		var $articles = document.querySelectorAll( '.ab-block-post-grid .is-grid article' );

		for ( i = 0; i < $articles.length; ++i ) {
			$date = $articles[i].querySelector( '.ab-block-post-grid-date' );
			$imageLink = $articles[i].querySelector( '.ab-block-post-grid-image a' );

			if ( $date && $imageLink ) {
				$imageLink.appendChild( $date );
			}
		}
	}

	moveDates();
}() );
