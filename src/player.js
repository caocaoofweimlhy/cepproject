var PlayerClass = cc.Sprite.extend({
    name: "player",
    game: null,
    world: null,
    pbody: null,
    pshape: null,
    playerSprite: null,
    jumprightSprite: null,
    jumpleftSprite: null,
    walkAction: null,
    jumprightAction: null,
    jumpleftAction: null,
    canJump: false,
    isAlive: true,
    ctor: function(game, gWorld, posX, posY) {
        this.game = game;
        this.world = gWorld;
        this.world.player = this;

        cc.spriteFrameCache.addSpriteFrames(res.walk_plist);
        this.spriteSheet = new cc.SpriteBatchNode(res.walk_png);
        this.addChild(this.spriteSheet);
        cc.spriteFrameCache.addSpriteFrames(res.jumpright_plist);
        this.jrspriteSheet = new cc.SpriteBatchNode(res.jumpright_png);
        this.addChild(this.jrspriteSheet);
        cc.spriteFrameCache.addSpriteFrames(res.jumpleft_plist);
        this.jlspriteSheet = new cc.SpriteBatchNode(res.jumpleft_png);
        this.addChild(this.jlspriteSheet);

        var walkFrames = [];
        var jumprightFrames = [];
        var jumpleftFrames = [];

        for (var i=1; i<5; i++){
            var str = "walkright"+i+".png";
            var frame = cc.spriteFrameCache.getSpriteFrame(str);
            walkFrames.push(frame);
        }
        for (var j=1; j<5; j++){
            var jrstr = "jumpright"+j+".png";
            var jrframe = cc.spriteFrameCache.getSpriteFrame(jrstr);
            jumprightFrames.push(jrframe);
        }
        for (var k = 1; k < 5; k++){
            var jlstr = "jumpleft"+k+".png";
            var jlframe = cc.spriteFrameCache.getSpriteFrame(jlstr);
            jumpleftFrames.push(jlframe);
        }

        var animation = new cc.Animation(walkFrames, 1);
        var jranimation = new cc.Animation(jumprightFrames, 0.2);
        var jlanimation = new cc.Animation(jumpleftFrames, 0.2);

        this.walkAction = new cc.RepeatForever(new cc.Animate(animation));
        this.jumprightAction = new cc.Repeat(new cc.Animate(jranimation),1);
        this.jumpleftAction = new cc.Repeat(new cc.Animate(jlanimation),1);
        
        this.playerSprite = new cc.Sprite.create(spriteImage);
        this.game.addChild(this.playerSprite,0);
        this.playerSprite.setPosition(posX,posY);
        var spriteImage = res.player_png;
        this.playerSprite.runAction(this.walkAction);
        this.spriteSheet.addChild(this.playerSprite);
        
        width = 30;
        height = 50;

        this.pbody = new cp.Body(1, Infinity);
        this.pbody.setPos(cp.v(posX, posY));
        this.world.addBody(this.pbody);

        this.pshape = this.world.addShape(new cp.BoxShape(this.pbody, width, height));
        this.pshape.setFriction(10.0);
        this.pshape.setElasticity(0.0);
        this.pshape.name = "player";
        this.pshape.id = 0;
        this.pshape.image = this.playerSprite;
        this.pshape.type = "player";

        this.pshape.setCollisionType("player");

    },

    startJumpright: function(curX, curY) {
        if(!this.canJump) {
            return 0;
        }

        this.canJump = false;

        this.playerSprite.runAction(this.jumprightAction);
        this.jrspriteSheet.addChild(this.playerSprite);
        this.pbody.applyImpulse(cp.v(100, 100), cp.v(curX, curY));
    },

    startJumpleft: function(curX, curY) {
        if(!this.canJump) {
            return 0;
        }

        this.canJump = false;

        this.playerSprite.runAction(this.jumpleftAction);
        this.jlspriteSheet.addChild(this.playerSprite);
        this.pbody.applyImpulse(cp.v(-100, 100), cp.v(curX, curY));
    },

    updatePosition: function() {
        this.pshape.image.x = this.pbody.p.x;
        this.pshape.image.y = this.pbody.p.y;
    },

    remove: function() {
        this.isAlive = false;
        this.world.removeBody(this.pbody);
        this.world.removeShape(this.pshape);
        this.game.removeChild(this.playerSprite);
    }
})